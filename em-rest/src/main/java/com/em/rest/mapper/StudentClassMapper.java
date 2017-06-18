package com.em.rest.mapper;

import com.em.rest.entity.T_class_student;
import org.apache.ibatis.annotations.Select;

import java.util.List;

/**
 * Created by litao on 2017/6/17.
 */
public interface StudentClassMapper {

    List<T_class_student> getStudentClass(int id);

}