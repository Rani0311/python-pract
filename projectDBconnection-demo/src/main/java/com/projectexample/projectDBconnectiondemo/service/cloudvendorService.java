package com.projectexample.projectDBconnectiondemo.service;

import com.projectexample.projectDBconnectiondemo.model.cloudvendor;

import java.util.List;

public interface cloudvendorService {
    public  String createcloudvendor(cloudvendor CloudVendor);
    public  String updatecloudvendor(cloudvendor Cloudvendor);
    public  String deletecloudvendor(String vendorid);
    public  cloudvendor getcloudvendor(String  vendorid);
    public List<cloudvendor> getallcloudvendor();

}
