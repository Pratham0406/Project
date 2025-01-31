async function getWeather() {
    const location = document.getElementById("location").value;
    const date = document.getElementById("date").value;
    
    if (!location || !date) {
        alert("Please enter a location and select a date.");
        return;
    }

    const apiKey = "YOUR_OPENWEATHERMAP_API_KEY"; // Replace with your API key
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(apiUrl);
        if (!response.ok) throw new Error("Location not found");

        const data = await response.json();
        document.getElementById("city").innerText = `Weather in ${data.name}`;
        document.getElementById("dateDisplay").innerText = `Date: ${date}`;
        document.getElementById("temperature").innerText = `Temperature: ${data.main.temp}°C`;
        document.getElementById("description").innerText = `Condition: ${data.weather[0].description}`;
    } catch (error) {
        alert("Error fetching weather data. Check the location.");
    }
}
