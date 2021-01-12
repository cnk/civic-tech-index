/*
 * import axios from "axios";
 * import MockAdapter from "axios-mock-adapter";
 * import cardImage from "./assets/images/broad.jpg"
 */

// mockAxios is supplied from the caller; dependency injection
const mockTag = (mockAxios) => {
  const API_REQUEST = "/api/blog/tags/";
  mockAxios.onGet(API_REQUEST).reply(200, {
    results: [
      { name: "Django", slug: "django" },
      { name: "React", slug: "react" },
      { name: "Wagtail", slug: "wagtail" },
    ],
  });
};

export { mockTag };
