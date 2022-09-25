import re
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import datetime

def home(request):
    return HttpResponse('''
    <html >
<body onLoad="initialize()">
                  <div class="col-sm-offset-1" id="map_canvas" style="width:500; height:500"></div>
                  <br>
                  <input type="text" id="lat">
                  <input type="text" id="lng">            
<script src="http://maps.google.com/maps/api/js?sensor=false" type="text/javascript"></script> 
<style>
  body{
    text-align:center;
  }
  .gmap3{
    margin: 20px auto;
    border: 1px dashed #C0C0C0;
    width: 500px;
    height: 500px;
  }
</style>    
<script type="text/javascript">
   var map;
 function initialize() {
 var myLatlng = new google.maps.LatLng(36.85341604753753,10.176080866332995);
 var myOptions = {
 zoom: 14,
 minZoom:14,
 center: myLatlng,
 draggable:false,
 mapTypeId: google.maps.MapTypeId.SATELLITE
 }
map = new google.maps.Map(document.getElementById("map_canvas"), myOptions); 
 var marker = new google.maps.Marker({
draggable: true,
position: myLatlng, 
map: map,
  });
google.maps.event.addListener(marker, 'dragend', function (event) {
document.getElementById("lat").value = this.getPosition().lat();
document.getElementById("lng").value = this.getPosition().lng();
}
); 
}
</script>
</body>
</html>
    ''')

def home2(request):
    return HttpResponse("Bienvenido a AI Way, tu aliado en mantenerte seguro")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )