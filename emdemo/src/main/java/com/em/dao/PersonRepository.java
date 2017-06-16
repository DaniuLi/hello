package com.em.dao;

import com.em.entity.Person;
import org.springframework.data.jpa.repository.JpaRepository;

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
}