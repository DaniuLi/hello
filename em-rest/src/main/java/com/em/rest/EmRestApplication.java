package com.em.rest;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.em.rest.mapper")
public class EmRestApplication {

	public static void main(String[] args) {
		SpringApplication.run(EmRestApplication.class, args);
	}
}
