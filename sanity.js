import sanityClient from "@sanity/client";
//import { SanityClient } from "@sanity/client";
import imageUrlBuilder from "@sanity/image-url";
//import { ImageUrlBuilder } from "@sanity/image-url/lib/types/builder";

const client = sanityClient({
    projectId: "zdpxja6a",
    dataset:"production",
    useCdn: true,
    apiVersion:"2021-03-25",
});

const builder = imageUrlBuilder(client);
export const urlFor = (source) => builder.image(source);

export default client;