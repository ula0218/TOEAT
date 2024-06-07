let map;
let currentPosition;
let currentPositionMarker;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 7,
    });
    navigator.geolocation.getCurrentPosition(function (position) {
        currentPosition = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };
        map.setCenter(currentPosition);
        map.setZoom(16);

        currentPositionMarker = new google.maps.Marker({
            position: currentPosition,
            map: map,
            title: "Your Current Location"
        });

        document.getElementById("map-loading").style.display = "none";
        document.getElementById("map").style.display = "block";
    });
}