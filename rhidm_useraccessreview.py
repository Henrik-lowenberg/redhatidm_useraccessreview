#!/usr/bin/python
# create local idm user api_reader
# create new role api-reader
# assign IPA Masters Readers to that role
# assign role to user
# login as user and set new pwd
# Read
# https://python-freeipa.readthedocs.io/en/latest/
#
# How-to install python-freeipa:
# pip install python-freeipa
#
# Import the freeipa library
from python_freeipa import ClientMeta
# pretty print to parse to human-readable output
import pprint
# parse json data
import json
 
# get login credentials
client = ClientMeta("idmreplica1.idm.example.com")
client.login("api-reader","apipwd")

# Get all IDM users
# use the freeipa module user_find method and store in userlist list
userlist = client.user_find()
#print userlist.items()
# get sub category result
userresult = userlist.get("result")
# declare empty list
listofusers = []
# pad the empty list with a header line
listofusers.append(['USER NAME', 'FULL NAME', 'GROUPS'])
# loop through each line in list
for row in userresult:
    # declare empty list where we inserts 3 elements of all user elements
    user = []
    user.append(row.get('uid')[0])
    user.append(row.get('cn')[0])
    user.append(row.get('memberof_group'))
    # add user list to bigger list of all users
    listofusers.append(user)
 
pretty_print = pprint.PrettyPrinter(indent=10,width=80,depth=None)
for row in listofusers:
#    print(row)
#    print(json.dumps(row))
    pretty_print.pprint(json.dumps(row))
 
print "\n"
 

# Get all user groups
#grouplist = client.group_find(posix=True)
grouplist = client.group_find()
#print grouplist.items()
groupresult = grouplist.get("result")
# Create empty list
listofgroups = []
listofgroups.append(['GROUP NAME', 'GROUP MEMBERSHIP', 'SUDORULE', 'HBACRULE'])
for row in groupresult:
    group = []
    group.append(row.get('cn')[0])
    group.append(row.get('memberof_group'))
#    group.append(row.get('memberofindirect_sudorule'))
    group.append(row.get('memberof_sudorule'))
    group.append(row.get('memberof_hbacrule'))
    listofgroups.append(group)
 
for row in listofgroups:
#    print(row)
    print(json.dumps(row))
 
print "\n"
 
# Get all host groups
hostgrouplist = client.hostgroup_find()
#print hostgrouplist.items()
hostgroupresult = hostgrouplist.get("result")
listofhostgroups = []
listofhostgroups.append(['HOSTGROUP NAME', 'HBACRULE MEMBERSHIP', 'HOSTS'])
for row in hostgroupresult:
    hostgroup = []
    hostgroup.append(row.get('cn')[0])
    hostgroup.append(row.get('memberof_hbacrule'))
    hostgroup.append(row.get('member_host'))
    listofhostgroups.append(hostgroup)
 
for row in listofhostgroups:
#    print(row)
    print(json.dumps(row))
 
print "\n"

 
# get all HBAC rules
hbacrulelist = client.hbacrule_find()
#print hbacrulelist.items()
hbacruleresult = hbacrulelist.get("result")
listofhbacrules = []
listofhbacrules.append(['HBACRULE NAME', 'MEMBER USER', 'TYPE OF ACCESS', 'MEMBER GROUP'])
for row in hbacruleresult:
    hbacrule = []
    hbacrule.append(row.get('cn')[0])
    hbacrule.append(row.get('memberuser_user'))
    hbacrule.append(row.get('accessruletype'))
    hbacrule.append(row.get('memberuser_group'))
    listofhbacrules.append(hbacrule)
 
for row in listofhbacrules:
#    print(row)
    print(json.dumps(row))
 
print "\n"
 
# get all Sudo rules
sudorulelist = client.sudorule_find()
#print sudorulelist
sudoruleresult = sudorulelist.get("result")
listofsudorules = []
listofsudorules.append(['SUDORULE NAME', 'RUN AS', 'MEMBER HOST', 'MEMBER USERGROUP', 'MEMBER HOSTGROUP', 'CMD CATEGORY'])
for row in sudoruleresult:
    sudorule = []
    sudorule.append(row.get('cn')[0])
    sudorule.append(row.get('ipasudorunasextuser'))
    sudorule.append(row.get('memberhost'))
    sudorule.append(row.get('memberuser_group'))
    sudorule.append(row.get('memberhost_hostgroup'))
    sudorule.append(row.get('cmdcategory'))
    listofsudorules.append(sudorule)
 
for row in listofsudorules:
#    print(row)
    print(json.dumps(row))
 
print "\n"
 
# get all Sudo commands
sudocmdlist = client.sudocmd_find()
#print sudocmdlist
sudocmdresult = sudocmdlist.get("result")
listofsudocmds = []
listofsudocmds.append(['SUDOCMD NAME', 'DESCRIPTION'])
for row in sudocmdresult:
    sudocmd = []
    sudocmd.append(row.get('sudocmd')[0])
    sudocmd.append(row.get('description'))
    listofsudocmds.append(sudocmd)
 
for row in listofsudocmds:
#    print(row)
    print(json.dumps(row))
 
print "\n"
 
# get all Sudo command groups
sudocmdgrouplist = client.sudocmdgroup_find()
#print sudocmdgrouplist
sudocmdresult = sudocmdgrouplist.get("result")
#type(sudocmdresult)
listofsudocmdgroups = []
listofsudocmdgroups.append(['SUDOCMDGROUP NAME', 'SUDO CMD'])

for row in sudocmdresult:
    sudocmdgroup = []
#    sudocmdgroup.append(row.get([0]))
    sudocmdgroup.append(row.get('cn'))
    sudocmdgroup.append(row.get('member_sudocmd'))
    listofsudocmdgroups.append(sudocmdgroup)
 
for row in listofsudocmdgroups:
#    print(row)
    print(json.dumps(row))
 
print "\n"

# END OF SCRIPT #