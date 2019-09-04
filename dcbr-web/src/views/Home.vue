<template>
  <v-container>
    <v-layout>
      <v-flex xs12 md4>
        <v-btn large round dark color="#fcba19" @click="$router.push('register')">Renew</v-btn>
      </v-flex>

      <v-flex>
        <v-btn large round block dark class="primary" @click="$router.push('preamble')">Register</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>
