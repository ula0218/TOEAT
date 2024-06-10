let map;
let currentPosition;
let currentPositionMarker;
let marker;
let directionsService;
let directionsRenderer;
let infoWindow;
let selectRestaurant;

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
            title: "Your Current Location",
            icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
        });

        const autocomplete = new google.maps.places.Autocomplete(
            document.getElementById('search-input'),
            {
                types:['restaurant'],
                bounds:{
                    east:currentPosition.lng+0.001,
                    west:currentPosition.lng-0.001,
                    south:currentPosition.lat-0.001,
                    north:currentPosition.lat+0.001,
                },
                strictBounds:false,
            }
        );
        autocomplete.addListener('place_changed',function(){
            const place = autocomplete.getPlace();
            
            selectRestaurant = {
                location : place.geometry.location,
                placeId : place.place_id,
                name : place.name,
                address : place.formatted_address,
                phoneNumber : place.formatted_phone_number,
                rating : place.rating,
            };
            console.log(selectRestaurant);
            
            map.setCenter(selectRestaurant.location);

            if(!marker){
                marker = new google.maps.Marker({
                    map: map,
                });
            }

            marker.setPosition(selectRestaurant.location);

            if(!directionsService){
                directionsService  = new google.maps.DirectionsService();
            }

            if(!directionsRenderer){
                directionsRenderer = new google.maps.DirectionsRenderer({
                    map: map,
                });
            }

            directionsRenderer.set('directions',null);
            
            directionsService.route(
                {
                    origin: new google.maps.LatLng(
                        currentPosition.lat,
                        currentPosition.lng
                    ),
                    destination:{
                        placeId:selectRestaurant.placeId,
                    },
                    travelMode:'WALKING',
                },
                function(response,status){
                    if(status == 'OK'){
                        directionsRenderer.setDirections(response);

                        if(!infoWindow){
                            infoWindow = new google.maps.InfoWindow();
                        }

                        infoWindow.setContent(`
                            <h3>${selectRestaurant.name}</h3>
                            <div>地址：${selectRestaurant.address}</div>
                            <div>電話：${selectRestaurant.phoneNumber}</div>
                            <div>評分：${selectRestaurant.rating}</div>
                            <div>步行時間：${response.routes[0].legs[0].duration.text}</div>
                        `);
                        infoWindow.open(map,marker);
                    }

                }
            );
        });

        document.getElementById("map-loading").style.display = "none";
        document.getElementById("map").style.display = "block";
        document.getElementById('clear-search').addEventListener('click', function() {
            document.getElementById('search-input').value = '';
        });
    });
}
