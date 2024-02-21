package com.Projectexample.projectdemo.model;

public class cloudvendor {
    String vendorid;
    String vendorname;
    String vendoraddress;
    String  vendorphonenumber;

    public String getVendorid() {
        return vendorid;
    }

    public void setVendorid(String vendorid) {
        this.vendorid = vendorid;
    }

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



    public cloudvendor() {
    }




    public cloudvendor(String vendorid, String vendorname, String vendoraddress, String vendorphonenumber) {
        this.vendorid = vendorid;
        this.vendorname = vendorname;
        this.vendoraddress = vendoraddress;
        this.vendorphonenumber = vendorphonenumber;
    }





}
