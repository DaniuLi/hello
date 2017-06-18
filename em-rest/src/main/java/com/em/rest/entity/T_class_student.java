package com.em.rest.entity;

import java.util.List;

public class T_class_student {
  private Long id;
  private String school_id;
  private String campus_id;
  private Long class_id;
  private String class_name;
  private Long student_id;
  private String name;
  private Long ispay;
  private Long paytype;
  private Long zks;
  private Long ywcks;
  private Double amount;
  private Double balance;
  private Long renewcount;
  private Long status;
  private String employee_id;
  private String employee_name;
  private Long parent_id;
  private String create_by;
  private java.sql.Timestamp create_date;
  private String update_by;
  private java.sql.Timestamp update_date;
  private String remarks;
  private String del_flag;

  public List<T_course_timetable> getCourses() {
    return courses;
  }

  public void setCourses(List<T_course_timetable> courses) {
    this.courses = courses;
  }

  private List<T_course_timetable> courses;

  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }

  public String getSchool_id() {
    return school_id;
  }

  public void setSchool_id(String school_id) {
    this.school_id = school_id;
  }

  public String getCampus_id() {
    return campus_id;
  }

  public void setCampus_id(String campus_id) {
    this.campus_id = campus_id;
  }

  public Long getClass_id() {
    return class_id;
  }

  public void setClass_id(Long class_id) {
    this.class_id = class_id;
  }

  public String getClass_name() {
    return class_name;
  }

  public void setClass_name(String class_name) {
    this.class_name = class_name;
  }

  public Long getStudent_id() {
    return student_id;
  }

  public void setStudent_id(Long student_id) {
    this.student_id = student_id;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public Long getIspay() {
    return ispay;
  }

  public void setIspay(Long ispay) {
    this.ispay = ispay;
  }

  public Long getPaytype() {
    return paytype;
  }

  public void setPaytype(Long paytype) {
    this.paytype = paytype;
  }

  public Long getZks() {
    return zks;
  }

  public void setZks(Long zks) {
    this.zks = zks;
  }

  public Long getYwcks() {
    return ywcks;
  }

  public void setYwcks(Long ywcks) {
    this.ywcks = ywcks;
  }

  public Double getAmount() {
    return amount;
  }

  public void setAmount(Double amount) {
    this.amount = amount;
  }

  public Double getBalance() {
    return balance;
  }

  public void setBalance(Double balance) {
    this.balance = balance;
  }

  public Long getRenewcount() {
    return renewcount;
  }

  public void setRenewcount(Long renewcount) {
    this.renewcount = renewcount;
  }

  public Long getStatus() {
    return status;
  }

  public void setStatus(Long status) {
    this.status = status;
  }

  public String getEmployee_id() {
    return employee_id;
  }

  public void setEmployee_id(String employee_id) {
    this.employee_id = employee_id;
  }

  public String getEmployee_name() {
    return employee_name;
  }

  public void setEmployee_name(String employee_name) {
    this.employee_name = employee_name;
  }

  public Long getParent_id() {
    return parent_id;
  }

  public void setParent_id(Long parent_id) {
    this.parent_id = parent_id;
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
