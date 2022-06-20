package com.fan.parseip.entity;

import com.baomidou.mybatisplus.annotation.TableName;

import lombok.Data;

@TableName("test_tb")
@Data
public class TestTb {
    private Integer id;
    private String srcIp;
    private String dstIp;
    private String srcLoc;
    private String dstLoc;
}
