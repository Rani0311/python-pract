package com.projectexample.projectDBconnectiondemo.service.impl;

import com.projectexample.projectDBconnectiondemo.model.cloudvendor;
import com.projectexample.projectDBconnectiondemo.repository.cloudvendorRespository;
import com.projectexample.projectDBconnectiondemo.service.cloudvendorService;

import java.util.List;

public class cloudvendorserviceimpl implements cloudvendorService {
    cloudvendorRespository  CloudVendorrespository;
    public cloudvendorserviceimpl(cloudvendorRespository cloudVendorrespository) {
        CloudVendorrespository = cloudVendorrespository;
    }


    @Override
    public String createcloudvendor(cloudvendor CloudVendor) {
        CloudVendorrespository.save(CloudVendor);
        return "save";
    }

    @Override
    public String updatecloudvendor(cloudvendor Cloudvendor) {
        CloudVendorrespository.save(Cloudvendor);
        return "success";
    }

    @Override
    public String deletecloudvendor(String vendorid) {
        CloudVendorrespository.deleteById(vendorid);
        return "success";
    }

    @Override
    public cloudvendor getcloudvendor(String vendorid) {

        return  CloudVendorrespository.findById(vendorid).get();
    }

    @Override
    public List<cloudvendor> getallcloudvendor() {
        return CloudVendorrespository.findAll();
    }
}
