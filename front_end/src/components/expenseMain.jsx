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


function ExpenseTable() {


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
                        <Tr>
                            <Td>Rona</Td>
                            <Td>10-09-2021</Td>
                            <Td>$20</Td>
                        </Tr>
                        <Tr>
                            <Td>Rona</Td>
                            <Td>10-09-2021</Td>
                            <Td>$20</Td>
                        </Tr>
                        <Tr>
                            <Td>Rona</Td>
                            <Td>10-09-2021</Td>
                            <Td>$20</Td>
                        </Tr>
                        <Tr>
                            <Td>Rona</Td>
                            <Td>10-09-2021</Td>
                            <Td>$20</Td>
                        </Tr>
                    </Tbody>
                </Table>
            </Box>
        </>
    )
}

export default ExpenseTable