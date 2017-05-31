//index.js
//获取应用实例
var app = getApp()
Page({
  data: {
    grids: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    motto: 'Hello World',
    defaultSize: 'default',
    primarySize: 'default',
    warnSize: 'default',
    disabled: false,
    plain: false,
    loading: false,
    userInfo: {}
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  //事件处理函数
  bindNewGroupButtonTap: function() {
    wx.navigateTo({
      url: '../group/group'
    })
  },
    //事件处理函数
  bindNewTaskButtonTap: function() {
    wx.navigateTo({
      url: '../task/task'
    })
  },
  onLoad: function () {
    console.log('onLoad')
    var that = this
    //调用应用实例的方法获取全局数据
    app.getUserInfo(function(userInfo){
      //更新数据
      that.setData({
        userInfo:userInfo
      })
    })
  }
})
