package com.em.rest.web;

import com.em.rest.entity.T_class_student;
import com.em.rest.mapper.StudentClassMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * Created by litao on 2017/6/17.
 */
@RestController
public class StudentClassController {
    @SuppressWarnings("SpringJavaAutowiringInspection")
    @Autowired
    private StudentClassMapper studentClassMapper;

    @RequestMapping("/getStudentClass")
    public List<T_class_student> getStudentClass(int id) {
        List<T_class_student> studentClasses= studentClassMapper.getStudentClass(id);
        return studentClasses;
    }


}
