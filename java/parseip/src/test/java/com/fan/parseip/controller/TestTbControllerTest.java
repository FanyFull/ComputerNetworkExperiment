package com.fan.parseip.controller;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class TestTbControllerTest {

    @Autowired
    private TestTbController testTbController;

    @Test
    public void testGetJson() {
        System.out.println("开始测试");
        testTbController.getJsonData();
    }

}
