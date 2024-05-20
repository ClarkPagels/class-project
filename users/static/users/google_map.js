let map;


async function initMap() {
 const position = { lat:38.0336, lng:-78.5080};


 const { Map } = await google.maps.importLibrary("maps");
 const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");


 map = new Map(document.getElementById("map"), {
   zoom: 15,
   center: position,
   mapId: "DEMO_MAP_ID",
 });
 const gas_marker = new google.maps.Marker({
    position: { lat: lat_a, lng: lng_a},
    map,

  });
 const activitiy_marker = new google.maps.Marker({
     position: {lat: lat_b, lng:lng_b},
     map,
 });
  const  restaurant_marker = new google.maps.Marker({
     position: {lat: lat_c, lng:lng_c},
     map,
 });
}


initMap();