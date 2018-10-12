# de-stress
Disaster Recovery Management Application - Code.fun.do.2018

"App to De-stress while in distress"

## Background :

Our society suffers a lot of damage because of various and complicated disasters. Many organizations are struggling to mitigate disasters to prevent a growing number of casualties.
Research on disaster risk warnings has been growing steadily. Even though at  present there are a number of places equipped with the warning systems, their not sufficient and efficient enough.

Our app focuses on bringing together affected people in times of disaster. This app has three primary objectives with a number of additional features that are essential for any disaster management app in general. We understand that the user or may or may not avail internet connectivity during such disasters, and accordingly developed the below three primary objectives.

## Primary Goals : 
 
### While not having proper internet connection  : 

#### Connect devices using WiFi hotspots and SSIDs :
During a disaster, any person would want to find other people nearby and move to safe place. Often it might so happen that, people might not be aware of other persons in their proximity. In such a scenario , the following is expected from our app : 
1. App will allow user to create a wifi hotspot.
2. The hotspot so created will have a ssid unique to each user.
3. This SSID will be linked to the user at the time of registration. At the time of registration all info will be uploaded to the server deployed in Microsoft Azure. 
4. The SSID is linked to the user, thus the app can access user details using the SSID. The SSID and corresponding minimal user data will be stored offline in a local database in the smartphone (which will be regularly synced with the online database. )
5. The app will scan for wifi connections in its vicinity, if it finds any, it will try to extract the user details using the ssid of the wifis available.
6. With this available data, a group of people can be brought together and a network can be formed where, the users can exchange information. This is elaborated in the next objective.
 
#### Create a peer-to-peer network communication using Wifi 
1. When offline (i.e no internet connection) , the app intends to form a mesh network of multiple app users, where minimal and necessary information/messages can be transmitted through wifi. 
2. It is basically a relay system, where information travels though wifi from one device to the next one in vicinity, thus spreading it in a simple and efficient manner. 
3. When the information reaches a device with proper internet connection. It can be transmitted to some other reliable source that can take proper action accordingly.
4. Establishing such a connection is the primary task, directing the messages to proper sources can be easily done by filtering the messages.





### While having proper internet connection :
1. Users can mark their location on the map and share them with others. This information can be shared with friends and relatives who can monitor the users location.
2. App will display on a map location of various people around the user and help people to form groups/communities.
3. Users can mark various areas on map as low, medium and high threat. This will inform other users which areas are safe and help them to find safe locations near them.
4. Upvote/downvote system where people present at affected areas can vote to verify the authenticity of a marker. Users can mark if shelters, food arrangements, medicines etc are present at particular areas. Others can upvote these locations to verify authenticity of the markers. 
5. Using the app, users can find short and safe paths to their desired locations.
If a user is under threat or needs food medicine urgently, he can mark his location along with description of situation on the map which can be viewed by others. This will help people involved in rescue operation to find people in distress.


## Additional features:
Users can store their personal information such as blood group, any serious medical diseases such as diabetics, contact numbers of relatives etc in the app. The case the user is found unconscious, this information can be used to provide correct treatment and contact his relatives.

