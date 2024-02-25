package com.projectexample.projectDBconnectiondemo.controller;

import com.projectexample.projectDBconnectiondemo.model.cloudvendor;

import com.projectexample.projectDBconnectiondemo.service.cloudvendorService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/cloudvendor")
public class cloudvendorAPIservices {
    cloudvendorService  CloudVendorservice;
    public cloudvendorAPIservices(cloudvendorService cloudVendorservice) {
        CloudVendorservice =cloudVendorservice;
    }

      //read specific vendor details
    @GetMapping("{vendorid}")
    public cloudvendor getcloudvendordetails(@PathVariable("vendorid")String vendorid)
    {


        return  CloudVendorservice.getcloudvendor(vendorid);
    }
    //read all vendor details
    @GetMapping()
    public List<cloudvendor> getallcloudvendordetails()
    {


        return  CloudVendorservice.getallcloudvendor();
    }
    @PostMapping
    public  String createvendordetails(@RequestBody cloudvendor CloudVendor)
    {
        CloudVendorservice.createcloudvendor(CloudVendor);
        return  "cloud vendor created";
    }
    @PutMapping
    public  String updatevendordetails(@RequestBody cloudvendor CloudVendor)
    {
        CloudVendorservice.updatecloudvendor(CloudVendor);
        return  "cloud vendor updated";
    }
    @DeleteMapping("vendorid")
    public  String deletevendordetails(@PathVariable("vendorid") String vendorid)
    {
        CloudVendorservice.deletecloudvendor(vendorid);

        return  "cloud vendor deleted";
    }


}
