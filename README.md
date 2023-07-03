# RobotFramework

robot -d Results --include=sanity Tagging.robot

robot -d results --variable server_name:10.10.10.10 --variable username:admin   --variable password:admin ssh_connection.robot 

robot -d Results -i sanity -i regression Tagging.robot

robot -d Results -e regression Tagging.robot

robot Reg*.robot

robot -d Results *.robot

pabot --processes 2 DDT*.robot

pabot --processes 2 --outputdir Results DDT*.robot



pip3 install requests

pip3 install robotframework-requests

pip3 show robotframework-requests

pip3 install robotframework-jsonlibrary 

pip3 install robotframework-seleniumlibrary

pip3 list

pip3 install robotframework-jsonlibrary==1.21

pip3 install —upgrade robotframework-jsonlibrary 
