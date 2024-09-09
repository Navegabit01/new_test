window.onload = function() {
    // Set the authorization header in Swagger UI
    SwaggerUIBundle({
        // Other Swagger UI settings
        spec: window.swaggerSpec,
        dom_id: '#swagger-ui',
        presets: [
            SwaggerUIBundle.presets.apis,
            SwaggerUIBundle.SwaggerUIStandalonePreset
        ],
        layout: "StandaloneLayout",
        // Add the JWT token input
        requestInterceptor: function(request) {
            var token = localStorage.getItem('jwt_token');
            if (token) {
                request.headers['Authorization'] = 'Bearer ' + token;
            }
            return request;
        }
    });
};
