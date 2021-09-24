import React from "react";
import {ChakraProvider, Box} from "@chakra-ui/react"

import ExpenseTable from "./components/expenseMain";


function App() {
  return (
    <ChakraProvider>
      <Box w={"100%"} m={0} p={0}>
        <ExpenseTable />
      </Box>
    </ChakraProvider>
  );
}

export default App;
