import React, { useState, useEffect } from "react"
import axios from 'axios'
import {ChakraProvider, Box} from "@chakra-ui/react"

import ExpenseTable from "./components/expenseMain";


function App() {

  const [expenseList, setExpenseList] = useState([{}])
  const [store, setStore] = useState('')
  const [date, setDate] = useState('')
  const [price, setPrice] = useState('')
  const fetchExpenses = async () => {
    const res = await fetch("http://127.0.0.1:8000/expenses")
    const expenses = await res.json()
    setExpenseList(expenses)
  }

  useEffect(() => {
    fetchExpenses()
  }, [])


  return (
    <ChakraProvider>
      <Box w={"100%"} m={0} p={0}>
        <ExpenseTable expenseList={ expenseList }/>
      </Box>
    </ChakraProvider>
  );
}

export default App;
