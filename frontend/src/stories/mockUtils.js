import axios from "axios";
import MockAdapter from "axios-mock-adapter";
// import cardImage from "./assets/images/broad.jpg"

// mockAxios is supplied from the caller; dependency injection
const mockTag = (mockAxios) => {
  const API_REQUEST = "/api/blog/tags/";
  mockAxios.onGet(API_REQUEST).reply(200, {
    results: [
      {slug: "django", name: "Django"},
      {slug: "react", name: "React"},
      {slug: "wagtail", name: "Wagtail"},
    ],
  });
};

const richtext1 = `
<p>Wagtail has been born out of many years of experience building websites, learning approaches that work and ones that don’t,
and striking a balance between power and simplicity, structure and flexibility. We hope you’ll find that Wagtail is in that sweet spot.</p>
`;


export { mockTag };
