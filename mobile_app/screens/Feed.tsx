import { useState } from 'react';
import { StyleSheet, FlatList, ListRenderItem } from 'react-native';

import { Text, View } from '../components/Themed';
import { Product, RootTabScreenProps } from '../types';

const DATA = [
  {
    id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
    title: 'First ItemAsdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd',
  },
  {
    id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
    title: 'Second Item',
  },
  {
    id: '58694a0f-3da1-471f-bd96-145571e29d72',
    title: 'Third Item',
  },
];

const ProductCard = ({ product }: { product: Product }) => (
  <View>
    <Text style={styles.title}>product.brand</Text>
  </View>
);

export default function Feed({ navigation }: RootTabScreenProps<'Feed'>) {
  const renderItem: ListRenderItem<Product> = ({ item }) => (
    <ProductCard product={item} />
  );

  const [products, setProducts] = useState<Product[]>([]);

  return (
    <View style={styles.container}>
      <FlatList data={products} renderItem={renderItem} keyExtractor={item => item.type} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});
