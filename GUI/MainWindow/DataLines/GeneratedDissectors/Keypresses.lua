-- Keypresses frame number-based postdissector
-- declare Fields to be read
-- declare our (pseudo) protocol
Keypresses_proto = Proto("keypresses","Keypresses Log")
-- create the fields for our "protocol"
timestamp_F = ProtoField.string("keypresses.timestamp","Original Event Timestamp")
eventdata_F = ProtoField.string("keypresses.data","Log Data")

-- add the field to the protocol
Keypresses_proto.fields = {timestamp_F, eventdata_F}

-- create a function to "postdissect" each frame
function Keypresses_proto.dissector(buffer,pinfo,tree)
    -- add the data based on timestamps
    if pinfo.abs_ts >= 1599083518.0 and pinfo.abs_ts <= 1599083520.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("ping oggl[BackSpace][BackSpace][BackSpace][BackSpace]gog[BackSpace]ogle.conm[BackSpace][BackSpace]m[Return]")

       subtree:add(timestamp_F,tostring("2020-09-02T21:51:58"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083525.0 and pinfo.abs_ts <= 1599083527.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("[Control_L]c")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:05"))
       subtree:add(eventdata_F, mycomplientstr)
    end
    if pinfo.abs_ts >= 1599083534.0 and pinfo.abs_ts <= 1599083536.0 then
       local subtree = tree:add(Keypresses_proto,"Keypresses Log")
       local mycomplientstr = tostring("find[Return][Control_L]")

       subtree:add(timestamp_F,tostring("2020-09-02T21:52:14"))
       subtree:add(eventdata_F, mycomplientstr)
    end
end
-- register our protocol as a postdissector
register_postdissector(Keypresses_proto)