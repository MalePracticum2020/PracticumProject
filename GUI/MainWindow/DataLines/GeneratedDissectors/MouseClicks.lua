-- MouseClicks frame number-based postdissector
-- declare Fields to be read
-- declare our (pseudo) protocol
MouseClicks_proto = Proto("mouseclicks","MouseClicks Log")
-- create the fields for our "protocol"
timestamp_F = ProtoField.string("mouseclicks.timestamp","Original Event Timestamp")
eventdata_F = ProtoField.string("mouseclicks.data","Log Data")

-- add the field to the protocol
MouseClicks_proto.fields = {timestamp_F, eventdata_F}

-- create a function to "postdissect" each frame
function MouseClicks_proto.dissector(buffer,pinfo,tree)
    -- add the data based on timestamps
    if pinfo.abs_ts >= 1599083546.0 and pinfo.abs_ts <= 1599083548.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083546.1921165_Navigator_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:26"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083510.0 and pinfo.abs_ts <= 1599083512.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083510.5694997_qterminal_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:51:50"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083540.0 and pinfo.abs_ts <= 1599083542.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083540.883116_wrapper-2.0_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:20"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083545.0 and pinfo.abs_ts <= 1599083547.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083545.774595_Navigator_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:25"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083547.0 and pinfo.abs_ts <= 1599083549.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083547.8195796_xfdesktop_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:27"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083527.0 and pinfo.abs_ts <= 1599083529.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083527.678454_qterminal_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:07"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083549.0 and pinfo.abs_ts <= 1599083551.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083549.1584918_xfdesktop_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:29"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083509.0 and pinfo.abs_ts <= 1599083511.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083509.1568034_main.py_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:51:49"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083547.0 and pinfo.abs_ts <= 1599083549.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083547.4249299_xfdesktop_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:27"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083528.0 and pinfo.abs_ts <= 1599083530.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083528.9538198_qterminal_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:08"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083551.0 and pinfo.abs_ts <= 1599083553.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083551.8851058_qterminal_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:31"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083552.0 and pinfo.abs_ts <= 1599083554.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083552.9949794_main.py_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:32"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083539.0 and pinfo.abs_ts <= 1599083541.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083539.0250273_qterminal_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:19"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083548.0 and pinfo.abs_ts <= 1599083550.0 then
       local subtree = tree:add(MouseClicks_proto,"MouseClicks Log")
       local mycomplientstr = tostring("/home/kali/eceld-netsys/eceld/plugins/collectors/pykeylogger/raw/click_images/1599083548.4909732_qterminal_root.png")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:28"))
       subtree:add(eventdata_F, mycomplientstr)
    end
end
-- register our protocol as a postdissector
register_postdissector(MouseClicks_proto)