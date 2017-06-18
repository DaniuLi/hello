package com.em.rest.entity;

public class T_course_timetable {
  private Long id;
  private Long school_id;
  private String campus_id;
  private Long subject_id;
  private Long class_id;
  private String class_desc;
  private java.sql.Date course_date;
  private java.sql.Timestamp begin_time;
  private java.sql.Timestamp end_time;
  private Long room_id;
  private String room_desc;
  private Long type;
  private Long status;
  private Long teacher_id;
  private String teacher_name;
  private Long p_id;
  private String create_by;
  private java.sql.Timestamp create_date;
  private String update_by;
  private java.sql.Timestamp update_date;
  private String remarks;
  private String del_flag;

  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }

  public Long getSchool_id() {
    return school_id;
  }

  public void setSchool_id(Long school_id) {
    this.school_id = school_id;
  }

  public String getCampus_id() {
    return campus_id;
  }

  public void setCampus_id(String campus_id) {
    this.campus_id = campus_id;
  }

  public Long getSubject_id() {
    return subject_id;
  }

  public void setSubject_id(Long subject_id) {
    this.subject_id = subject_id;
  }

  public Long getClass_id() {
    return class_id;
  }

  public void setClass_id(Long class_id) {
    this.class_id = class_id;
  }

  public String getClass_desc() {
    return class_desc;
  }

  public void setClass_desc(String class_desc) {
    this.class_desc = class_desc;
  }

  public java.sql.Date getCourse_date() {
    return course_date;
  }

  public void setCourse_date(java.sql.Date course_date) {
    this.course_date = course_date;
  }

  public java.sql.Timestamp getBegin_time() {
    return begin_time;
  }

  public void setBegin_time(java.sql.Timestamp begin_time) {
    this.begin_time = begin_time;
  }

  public java.sql.Timestamp getEnd_time() {
    return end_time;
  }

  public void setEnd_time(java.sql.Timestamp end_time) {
    this.end_time = end_time;
  }

  public Long getRoom_id() {
    return room_id;
  }

  public void setRoom_id(Long room_id) {
    this.room_id = room_id;
  }

  public String getRoom_desc() {
    return room_desc;
  }

  public void setRoom_desc(String room_desc) {
    this.room_desc = room_desc;
  }

  public Long getType() {
    return type;
  }

  public void setType(Long type) {
    this.type = type;
  }

  public Long getStatus() {
    return status;
  }

  public void setStatus(Long status) {
    this.status = status;
  }

  public Long getTeacher_id() {
    return teacher_id;
  }

  public void setTeacher_id(Long teacher_id) {
    this.teacher_id = teacher_id;
  }

  public String getTeacher_name() {
    return teacher_name;
  }

  public void setTeacher_name(String teacher_name) {
    this.teacher_name = teacher_name;
  }

  public Long getP_id() {
    return p_id;
  }

  public void setP_id(Long p_id) {
    this.p_id = p_id;
  }

  public String getCreate_by() {
    return create_by;
  }

  public void setCreate_by(String create_by) {
    this.create_by = create_by;
  }

  public java.sql.Timestamp getCreate_date() {
    return create_date;
  }

  public void setCreate_date(java.sql.Timestamp create_date) {
    this.create_date = create_date;
  }

  public String getUpdate_by() {
    return update_by;
  }

  public void setUpdate_by(String update_by) {
    this.update_by = update_by;
  }

  public java.sql.Timestamp getUpdate_date() {
    return update_date;
  }

  public void setUpdate_date(java.sql.Timestamp update_date) {
    this.update_date = update_date;
  }

  public String getRemarks() {
    return remarks;
  }

  public void setRemarks(String remarks) {
    this.remarks = remarks;
  }

  public String getDel_flag() {
    return del_flag;
  }

  public void setDel_flag(String del_flag) {
    this.del_flag = del_flag;
  }
}
