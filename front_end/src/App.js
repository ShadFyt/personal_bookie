import React from "react";
import {ChakraProvider, Box} from "@chakra-ui/react"

function App() {
  return (
    <ChakraProvider>
      <Box><h1>HELLO WORLD</h1></Box>
    </ChakraProvider>
  );
}

export default App;
