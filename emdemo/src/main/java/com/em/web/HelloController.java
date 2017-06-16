package com.em.web;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by 0216000543 on 2017/6/15.
 */
@RestController
public class HelloController {
    @RequestMapping("/hello")
    public String say(){
        return "Hello SpringBoot!";
    }
}
