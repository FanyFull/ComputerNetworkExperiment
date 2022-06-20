package com.fan.parseip.service.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.fan.parseip.entity.TestTb;
import com.fan.parseip.mapper.TestTbMapper;
import com.fan.parseip.service.ITestTbService;

@Service("testTbService")
public class ITestTbServiceImpl extends ServiceImpl<TestTbMapper, TestTb> implements ITestTbService {

    @Autowired
    private TestTbMapper testTbMapper;

}
