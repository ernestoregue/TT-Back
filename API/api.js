const API = "http://127.0.0.1:5000/map-api"
let markersPlaces = [new atlas.data.Feature(new atlas.data.Point([-122.3802, 47.54384]), {
    myRadius: 30,
    category: 'posi',
    textField: 'Holi'
})];
/* Define async function */
async function getPlaceData() {
    const response = await fetch(API);
    const data = await response.json();
    // foreach loop to get all the data
    data.places.forEach((place) => {
            //Has myRadius and category value.
            
        // add data to markersPlaces
        markersPlaces.push(new atlas.data.Feature(new atlas.data.Point([Number(place.latitude), Number(place.longitude)]), {
            myRadius: 30,
            category: 'posi',
            textField: place.name
        }));
        
    });

    return data;
}

window.addEventListener('load', function () {
    getPlaceData();
    console.log(markersPlaces);
    // foreach loop to get all the data from markersPlaces
});