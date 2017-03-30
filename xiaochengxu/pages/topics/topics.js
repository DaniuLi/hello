// pages/topics/topics.js
var Api = require('../../utils/api.js');
var util = require('../../utils/util.js');

Page({
  data:{
    title:'作业列表',
    topicsList: [{
      "id": "1",
      "author_id": "1",
      "tab": "share",
      "content": "<div class=\"markdown-text\">继续完善文档，沉淀最佳实践，并帮助社区产出更多的插件和上层框架。<</div>",
      "title": "4月1日打卡内容",
      "last_reply_at": "1小时前",
      "good": false,
      "top": false,
      "reply_count": 63,
      "visit_count": 3197,
      "create_at": "2017-03-21T10:06:45.487Z",
      "author": {
        "loginname": "litao",
        "avatar_url": "https://avatars.githubusercontent.com/u/227713?v=3&s=120"
      }
    },
    {
      "id": "2",
      "author_id": "2",
      "tab": "share",
      "content": "<div class=\"markdown-text\">如果有比较好的<code>问题/知识点/指正</code>，也欢迎提 PR。</p>\n<p>另外关于 <code>Js 基础</code> 是个比较大的话题，在本教程不会很细致深入的讨论，更多的是列出一些重要或者更服务端更相关的地方，所以如果你拿着《JavaScript 权威指南》给教程提 PR 可能不会采纳。本教程的重点更准确的说是服务端基础中 Node.js 程序员需要了解的部分。</div>",
      "title": "4月2日打卡内容",
      "last_reply_at": "6小时前",
      "good": false,
      "top": false,
      "reply_count": 88,
      "visit_count": 14769,
      "create_at": "2017-02-22T11:32:43.547Z",
      "author": {
        "loginname": "taoli",
        "avatar_url": "https://avatars1.githubusercontent.com/u/2081487?v=3&s=120"
      }
    }],
    postsList: [{
      "id": "1",
      "author_id": "1",
      "tab": "share",
      "content": "<div class=\"markdown-text\">继续完善文档，沉淀最佳实践，并帮助社区产出更多的插件和上层框架。<</div>",
      "title": "4月1日打卡内容",
      "last_reply_at": "1小时前",
      "good": false,
      "top": false,
      "reply_count": 63,
      "visit_count": 3197,
      "create_at": "2017-03-21T10:06:45.487Z",
      "author": {
        "loginname": "litao",
        "avatar_url": "https://avatars.githubusercontent.com/u/227713?v=3&s=120"
      }
    },
    {
      "id": "2",
      "author_id": "2",
      "tab": "share",
      "content": "<div class=\"markdown-text\">如果有比较好的<code>问题/知识点/指正</code>，也欢迎提 PR。</p>\n<p>另外关于 <code>Js 基础</code> 是个比较大的话题，在本教程不会很细致深入的讨论，更多的是列出一些重要或者更服务端更相关的地方，所以如果你拿着《JavaScript 权威指南》给教程提 PR 可能不会采纳。本教程的重点更准确的说是服务端基础中 Node.js 程序员需要了解的部分。</div>",
      "title": "4月2日打卡内容",
      "last_reply_at": "6小时前",
      "good": false,
      "top": false,
      "reply_count": 88,
      "visit_count": 14769,
      "create_at": "2017-02-22T11:32:43.547Z",
      "author": {
        "loginname": "taoli",
        "avatar_url": "https://avatars1.githubusercontent.com/u/2081487?v=3&s=120"
      }
    }],
    hidden: true,
    topBarItems: [
      // id name selected 选中状态
      {id:'all',name:'作业列表',selected:true},
      {id:'good',name:'已交作业',selected:false},
      {id:'ask',name:'问答',selected:false},
    ],
    page: 1,
    tab: 'all'
  },
  onLoad:function(options){
    // 页面初始化 options为页面跳转所带来的参数
    console.log('onload by topics...');
    //this.hidden = true;
    //this.fetchData();// 获取数据
  },
  onPullDownRefresh: function () {
    //this.fetchData();
    console.log('下拉刷新', new Date());
  },
  onTapTag: function (e) {
    var self = this;
    var tab = e.currentTarget.id;
    var topBarItems = self.data.topBarItems;
    // 切换topBarItem 
    for (var i = 0;i<topBarItems.length;i++) {
      if(tab == topBarItems[i].id) {
          topBarItems[i].selected = true;
      } else {
          topBarItems[i].selected = false;
      }
    }
    self.setData({
      topBarItems:topBarItems
    })

    self.setData({
      tab: tab
    });
    if (tab !== 'all') {
      //this.fetchData({tab: tab});
    } else {
      //this.fetchData();
    }

  },
  onReady:function(){
    // 页面渲染完成
  },
  onShow:function(){
    // 页面显示
  },
  onHide:function(){
    // 页面隐藏
  },
  onUnload:function(){
    // 页面关闭
  },
  fetchData: function (data) {
    var self = this;
    self.setData({
      hidden: false
    });
    if (!data) data = {};
    if (!data.page) data.page = 1;
    if (data.page === 1) {
      self.setData({
        postsList: []
      });
    }
    wx.request({
      url: Api.getTopics(data),
      success: function (res) {
        self.setData({
          postsList: self.data.postsList.concat(res.data.data.map(function (item) {
            item.last_reply_at = util.getDateDiff(new Date(item.last_reply_at));
            return item;
          }))
        });
        setTimeout(function () {
          self.setData({
            hidden: true
          });
        }, 300);
      }
    });
  },
  redictDetail: function (e) {
    console.log('我要看详情');
    var id = e.currentTarget.id,
        url = '../detail/detail?id=' + id;
    wx.navigateTo({
      url: url
    })
  },
  lower: function (e) {
    var self = this;
    self.setData({
      page: self.data.page + 1
    });
    if (self.data.tab !== 'all') {
      //this.fetchData({tab: self.data.tab, page: self.data.page});
    } else {
      //this.fetchData({page: self.data.page});
    }
  }
})