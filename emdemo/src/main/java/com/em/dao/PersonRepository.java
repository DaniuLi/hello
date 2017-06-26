package com.em.dao;

import com.em.entity.ClassInfo;
import com.em.entity.Person;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

/**
 * Created by litao on 2017/6/15.
 */
public interface PersonRepository extends JpaRepository<Person,Integer> {
    /**
     *  通过年龄来查询
     *  方法名固定findByAge
     * @param age
     * @return
     */
    public List<Person> findByAge(Integer age);

    @Query("select distinct A.class_name, A.zks, A.ywcks, A.school_id, A.campus_id, B.teacher_name, B.class_id from t_class_student A, t_course_timetable B where A.student_id = 2 and A.class_id = B.class_id")
    public List<ClassInfo> findAllClass();
}