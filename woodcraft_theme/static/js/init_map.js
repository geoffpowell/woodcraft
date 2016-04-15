var latitude;
var longitude;

function initMap() {
  	var myLocation = {lat: latitude, lng: longitude};
    var mapDiv = document.getElementById('map');
    var map = new google.maps.Map(mapDiv, {
      center: myLocation,
      zoom: 14,
      mapTypeId: google.maps.MapTypeId.TERRAIN
    });
    var marker = new google.maps.Marker({
      position: myLocation,
      map: map,
      title: 'Pura Vida Surf Shop'
  	});
  }

// var address_string = $("address a").val();
var address_string = ($("address a").html());


$.ajax({
		url: "http://maps.google.com/maps/api/geocode/json?address=" + address_string +"&sensor=false",
		success: function(data){
			console.log(data);
			// console.log(data.results[0].geometry["location"].lat);
			latitude = (data.results[0].geometry["location"].lat);

			// console.log(data.results[0].geometry["location"].lng);
			longitude = (data.results[0].geometry["location"].lng);
			initMap();
	  }
	});

// function initMap() {
//   var map = new google.maps.Map(document.getElementById('map'), {
//     zoom: 8,
//     center: {lat: 45, lng: -120}
//   });
//   var geocoder = new google.maps.Geocoder();

  
// }

// function geocodeAddress(geocoder, resultsMap) {
//   var address = "2102 Jackson St SE, Albany, OR, 97322";
//   geocoder.geocode({'address': address}, function(results, status) {

//     if (status === google.maps.GeocoderStatus.OK) {
//       resultsMap.setCenter(results[0].geometry.location);
//       var marker = new google.maps.Marker({
//         map: resultsMap,
//         position: results[0].geometry.location
//       });
//     } else {
//       alert('Geocode was not successful for the following reason: ' + status);
//     }
//   });
// }
