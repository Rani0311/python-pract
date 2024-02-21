package com.Projectexample.projectdemo.controller;

import com.Projectexample.projectdemo.model.cloudvendor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/cloudvender")
public class cloudAPIservice {
    cloudvendor CloudVendor;
  @GetMapping("{vendorid}")
    public cloudvendor getcloudvendordetails(String vendorid)
    {
        return  new cloudvendor("c1","ABC","India","XXXX");
    }
    @PostMapping
    public  String createvendordetails(@RequestBody cloudvendor CloudVendor)
    {
        this.CloudVendor=CloudVendor;
        return  "cloud vendor created";
    }
    @PutMapping
    public  String updatevendordetails(@RequestBody cloudvendor CloudVendor)
    {
        this.CloudVendor=CloudVendor;
        return  "cloud vendor updated";
    }
    @DeleteMapping("vendorid")
    public  String deletevendordetails(@RequestBody cloudvendor CloudVendor)
    {
        this.CloudVendor=null;
        return  "cloud vendor deleted";
    }


}
