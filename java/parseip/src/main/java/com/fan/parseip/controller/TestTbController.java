package com.fan.parseip.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.fan.parseip.entity.TestTb;
import com.fan.parseip.service.ITestTbService;

@CrossOrigin(originPatterns = "*", maxAge = 3600) // 配置跨域
@RestController
@RequestMapping("/testTb")
public class TestTbController {

    @Autowired
    private ITestTbService testTbService;

    @GetMapping("/findAll")
    public List<TestTb> findAllItems() {
        QueryWrapper<TestTb> wrapper = new QueryWrapper<>();
        wrapper.orderByAsc("id");
        // 使用 last 方法拼接 sql 语句
        wrapper.last("limit 100");
        // 先取出一定数量的数据
        List<TestTb> testTbList = testTbService.list(wrapper);
        List<Integer> idList = new ArrayList<>();
        for (TestTb testTb : testTbList) {
            idList.add(testTb.getId());
        }
        // testTbService.removeBatchByIds(idList);
        return testTbList;
    }

    /**
     * 过滤出同时具有 srcLoc 和 dstLoc 并且都是中国城市的数据
     * 
     * @return
     * @throws IOException
     * @throws InterruptedException
     */
    @GetMapping("/getJson")
    public List<TestTb> getJsonData() {
        // 先从数据库中取出数据
        List<TestTb> testTbList = testTbService.list();
        List<TestTb> filtedList = new ArrayList<>();

        // 过滤
        for (TestTb testTb : testTbList) {
            if (testTb.getSrcLoc() != null
                    && testTb.getSrcLoc().length() != 0
                    && !testTb.getSrcLoc().equals("海外")
                    && testTb.getDstLoc() != null
                    && testTb.getDstLoc().length() != 0
                    && !testTb.getDstLoc().equals("海外")) {
                filtedList.add(testTb);
                System.out.println(testTb);
            }
        }
        // System.out.println(filtedList);

        return filtedList;
    }

}
