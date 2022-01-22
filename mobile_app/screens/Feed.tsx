import { useState } from 'react';
import { StyleSheet, ListRenderItem } from 'react-native';

import { Product, RootTabScreenProps } from '../types';

import { Image, FlatList, Text, Box, AspectRatio, Center, Stack, Heading, HStack } from "native-base";

import axios from 'axios';

const ProductCard = ({ product }: { product: Product }) => (
  <Box
  maxW="80"
  rounded="lg"
  overflow="hidden"
  borderColor="coolGray.200"
  borderWidth="1"
  _dark={{
    borderColor: "coolGray.600",
    backgroundColor: "gray.700",
  }}
  _web={{
    shadow: 2,
    borderWidth: 0,
  }}
  _light={{
    backgroundColor: "gray.50",
  }}
  marginBottom={5}
>
  <Box>
    <AspectRatio w="100%" ratio={16 / 9}>
      <Image
        source={{
          uri: "https://i.imgur.com/jc5dIwW.jpg",
        }}
        alt="image"
      />
    </AspectRatio>
    <Center
      bg="blue.500"
      _dark={{
        bg: "blue.400",
      }}
      _text={{
        color: "warmGray.50",
        fontWeight: "700",
        fontSize: "xs",
      }}
      position="absolute"
      bottom="0"
      px="3"
      py="1.5"
    >
      Price: 15£
    </Center>
  </Box>
  <Stack p="4" space={3}>
    <Stack space={2}>
      <Heading size="md" ml="-1">
        Asos - Blue coat
      </Heading>
      <Text
        fontSize="xs"
        _light={{
          color: "blue.500",
        }}
        _dark={{
          color: "blue.400",
        }}
        fontWeight="500"
        ml="-0.5"
        mt="-1"
      >
        New
      </Text>
    </Stack>
    <Text fontWeight="400">
      For sale in asdasdasljd
    </Text>
    <HStack alignItems="center" space={4} justifyContent="space-between">
      <HStack alignItems="center">
        <Text
          color="coolGray.600"
          _dark={{
            color: "warmGray.200",
          }}
          fontWeight="400"
        >
          6 mins ago
        </Text>
      </HStack>
    </HStack>
  </Stack>
</Box>
);

export default function Feed({ navigation }: RootTabScreenProps<'Feed'>) {
  const renderItem: ListRenderItem<Product> = ({ item }) => (
    <ProductCard product={item} />
  );

  const [products, setProducts] = useState<Product[]>([
    {
      colour: "red",
      brand: "Nike",
      type: "Shoes",
      price: 200,
      condition: "New",
      gender: 'f'
    },
    {
      colour: "red",
      brand: "Nike",
      type: "a",
      price: 200,
      condition: "New",
      gender: 'f'
    },
    {
      colour: "red",
      brand: "Nike",
      type: "b",
      price: 200,
      condition: "New",
      gender: 'f'
    }
  ]);

  return (
    <Center>
      <FlatList data={products} renderItem={renderItem} keyExtractor={item => item.type} />
    </Center>
  );
}