package com.em.entity;

import javax.persistence.Entity;

/**
 * Created by litao on 2017/6/16.
 */
@Entity
public class ClassInfo {
    public ClassInfo() {
    }

    private String school_id;
    private String campus_id;
    private Long class_id;
    private String class_name;
    private Long zks;
    private Long ywcks;

    public String getTeacher_name() {
        return teacher_name;
    }

    public void setTeacher_name(String teacher_name) {
        this.teacher_name = teacher_name;
    }

    private String teacher_name;

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


}
