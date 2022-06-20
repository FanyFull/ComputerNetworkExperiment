package com.fan.parseip;

import java.io.IOException;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.fan.parseip.mapper")
public class ParseipApplication {

    public static void main(String[] args) throws IOException, InterruptedException {
        SpringApplication.run(ParseipApplication.class, args);
    }

}
