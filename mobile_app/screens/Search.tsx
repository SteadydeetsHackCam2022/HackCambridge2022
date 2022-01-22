import { StyleSheet } from 'react-native';

import { RootTabScreenProps } from '../types';

import { Camera } from 'expo-camera';
import { useEffect, useState } from 'react';
import { Box } from 'native-base';

export default function Search({ navigation }: RootTabScreenProps<'Search'>) {
  // const [hasPermission, setHasPermission] = useState<null | boolean>(null);
  // const [type, setType] = useState(Camera.Constants.Type.front);

  // useEffect(() => {
  //   (async () => {
  //     const { status } = await Camera.requestCameraPermissionsAsync();
  //     setHasPermission(status === 'granted');
  //     console.log(status);
  //   })();
  // }, []);

  return (
    <Box>
{/* <Camera type={type}>
    </Camera> */}
    </Box>
  );
}