package com.projectexample.projectDBconnectiondemo.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name="cloud_vendor_info")
public class cloudvendor {
    @Id
    String vendorname;
    String vendoraddress;
    String  vendorphonenumber;
    String vendorid;


    public String getVendorname() {
        return vendorname;
    }

    public void setVendorname(String vendorname) {
        this.vendorname = vendorname;
    }

    public String getVendoraddress() {
        return vendoraddress;
    }

    public void setVendoraddress(String vendoraddress) {
        this.vendoraddress = vendoraddress;
    }

    public String getVendorphonenumber() {
        return vendorphonenumber;
    }

    public void setVendorphonenumber(String vendorphonenumber) {
        this.vendorphonenumber = vendorphonenumber;
    }

    public String getVendorid() {
        return vendorid;
    }

    public void setVendorid(String vendorid) {
        this.vendorid = vendorid;
    }


    public cloudvendor() {
    }

    public cloudvendor(String vendorname, String vendoraddress, String vendorphonenumber, String vendorid) {
        this.vendorname = vendorname;
        this.vendoraddress = vendoraddress;
        this.vendorphonenumber = vendorphonenumber;
        this.vendorid = vendorid;
    }







}
