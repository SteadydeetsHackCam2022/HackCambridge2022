import React from "react"
import { StyleSheet, TextInput } from 'react-native';
import { Input, Button, Icon, Stack, Text, Center, NativeBaseProvider } from "native-base";
import { MaterialIcons } from "@expo/vector-icons";

export const Example = () => {
    return (
        <>
        <Text style={styles.title}>Sign up here</Text>
        <TextInput 
          style={styles.inputbox}
          defaultValue="Email"  
        />
        </>
    )
}
/*export const Example = () => {
  return (
    <>
    <>
    <Text>Test</Text>
    </>
    <Stack space={4} w="100%" alignItems="center">
      <Input
        w={{
          base: "75%",
          md: "25%",
        }}
        InputLeftElement={
          <Icon
            as={<MaterialIcons name="person" />}
            size={5}
            ml="2"
            color="muted.400"
          />
        }
        placeholder="Email"
      />
      <Input
        w={{
          base: "75%",
          md: "25%",
        }}
        InputRightElement={
          <Icon
            as={<MaterialIcons name="visibility-off" />}
            size={5}
            mr="2"
            color="muted.400"
          />
        }
        placeholder="Password"
      />
    </Stack>
    <>
      <Button onPress={() => console.log("hello world")}>Sign Up</Button>
    </>
    </>
  )
}
*/

const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center',
    },
    title: {
      fontSize: 20,
      color: 'white',
      fontWeight: 'bold',
    },
    separator: {
      marginVertical: 30,
      height: 1,
      width: '80%',
    },
    inputbox: {
      height: 40,
      borderColor: 'gray',
      borderWidth: 1,
      color: 'white'
    }
  });

export default () => {
  return (
    <NativeBaseProvider>
      <Center flex={1} px="3">
        <Example />
      </Center>
    </NativeBaseProvider>
  )
}