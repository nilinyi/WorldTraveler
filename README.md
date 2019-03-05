
WorldTraveler
-------------
Make a fake location in your REAL iOS device.  
## Usage
**Firstly**, you need to have Xcode installed in your Mac.  
**Secondly**, open the project "WorldTraveler.xcodeproj".  
**Thirdly**, plug in your iOS device to computer and press Command+R to run your program(You might need to change the simulation target. Product -> Destination -> Your device). You need to make sure your iOS device is properly configured that it can accept the app installed from XCode. (General -> Profiles & Device Management -> Developer App -> Trust)  
**Finally**, change the location.  
<br> 
<img src="2.png">
<br> 
<br> 
   
Now! Don't plug out your device! Just press your home button and open a social media app like Facebook. You can see your location has been changed to Sydney Opera House!  
<br> 
<img src="3.pic.jpg" width="250">

## Customize your location
Open FakeLocation.gpx in Xcode and change the value of "lat" and "lon" in this file. Save the file and do the last step above again.
<img src="4.png">

## Advanced: Simulate continuous GPS change
Your location right now is static. Because Xcode just simply read and set the location from the location file. How to simulate that we're actually moving, a.k.a, chaning the location continuously? It's very simple actually. We just need a script to keep reading and loading the location file, which can be updated in the background by other services.
