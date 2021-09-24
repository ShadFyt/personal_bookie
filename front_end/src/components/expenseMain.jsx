import React, { useState, useEffect } from "react"
import axios from 'axios'

import {
    Box,
    Button,
    Table,
    Thead,
    Tbody,
    Tfoot,
    Tr,
    Th,
    Td,
    TableCaption,

} from "@chakra-ui/react"



function ExpenseTable({ expenseList }) {

    function ExpenseWrapper({ expense }) {
        console.log(expense)
        return (
            <Tr>
                <Th>{expense.store}</Th>
                <Th>{expense.date}</Th>
                <Th>{expense.price}</Th>
            </Tr>
        )
    }

    return (
        <>
            <Box d={"flex"} as={"main"} w={"75%"} mx={"auto"} mt={6}>
                <Table variant={"simple"}>
                    <TableCaption>Last 100 expenses.</TableCaption>
                    <Thead>
                        <Tr>
                            <Th>Store</Th>
                            <Th>Date of purchase</Th>
                            <Th>Cost</Th>
                        </Tr>
                    </Thead>
                    <Tbody>
                        {expenseList.map(expense => <ExpenseWrapper expense={expense} />)}
                    </Tbody>
                </Table>
            </Box>
        </>
    )
}

export default ExpenseTable