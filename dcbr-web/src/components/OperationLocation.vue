<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <!-- <v-card-title primary-title>
        <h2>Operation Location(s)</h2>
      </v-card-title>-->
      <v-flex xs12>
        <v-card flat>
          <v-form v-model="valid">
            <v-container>
              <!-- Home address section  -->

              <v-layout row mt-3 mx-2>
                <h4>Address {{number+1}}</h4>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="streetNumber"
                    :rules="streetNumberRules"
                    label="Street number"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4 lg6>
                  <v-text-field v-model="aptNumber" label="Apt/Suite" required></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="streetName"
                    :rules="nameRules"
                    label="Street name"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field v-model="city" :rules="nameRules" label="City" required></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="postalCode"
                    :rules="nameRules"
                    label="Postal Code"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-col class="d-flex" cols="12" sm="6">
                    <v-select :items="items" label="Region"></v-select>
                  </v-col>
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import { mapState } from "vuex";
export default {
  props: ["number"],
  data: () => ({
    items: [
      "Alberni-Clayoquot ",
      "Bulkley-Nechako ",
      "Capital ",
      "Cariboo ",
      "Central Coast ",
      "Central Okanagan   ",
      "Columbia Shuswap  ",
      "Comox Valley  ",
      "Cowichan Valley  ",
      "East Kootenay  ",
      "Fraser Valley  ",
      "Fraser-Fort George  ",
      "Islands Trust  ",
      "Kitimat-Stikine  ",
      "Kootenay-Boundary  ",
      "Metro Vancouver  ",
      "Mount Waddington  ",
      "Nanaimo  ",
      "North Okanagan ",
      "North Coast ",
      "Okanagan-Similkameen  ",
      "Peace River  ",
      "qathet ",
      "Squamish-Lillooet  ",
      "Strathcona  ",
      "Sunshine Coast  River  ",
      "Thompson-Nicola "
    ],
    valid: false,
    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],
    streetNumberRules: [v => !!v || "Street number is required"]
  }),
  methods: {},
  computed: {
    ...mapState({
      operationLocations: state => state.operationLocations
    }),
    streetName: {
      // getter
      get() {
        return this.$store.getters["operationLocations/locations"][
          this.$props.number
        ].streetName;
      },
      // setter
      set(value) {
        this.$store.dispatch("operationLocations/updateLocationProperty", {
          index: this.$props.number,
          property: "streetName",
          value: value
        });
      }
    },
    aptNumber: {
      // getter
      get() {
        return this.$store.getters["operationLocations/locations"][
          this.$props.number
        ].aptNumber;
      },
      // setter
      set(value) {
        this.$store.dispatch("operationLocations/updateLocationProperty", {
          index: this.$props.number,
          property: "aptNumber",
          value: value
        });
      }
    },
    streetNumber: {
      // getter
      get() {
        return (
          this.$store.getters["operationLocations/locations"][
            this.$props.number
          ].streetNumber || ""
        );
      },
      // setter
      set(value) {
        this.$store.dispatch("operationLocations/updateLocationProperty", {
          index: this.$props.number,
          property: "streetNumber",
          value: value
        });
      }
    },
    city: {
      // getter
      get() {
        return this.$store.getters["operationLocations/locations"][
          this.$props.number
        ].city;
      },
      // setter
      set(value) {
        this.$store.dispatch("operationLocations/updateLocationProperty", {
          index: this.$props.number,
          property: "city",
          value: value
        });
      }
    },
    postalCode: {
      // getter
      get() {
        return this.$store.getters["operationLocations/locations"][
          this.$props.number
        ].postalCode;
      },
      // setter
      set(value) {
        this.$store.dispatch("operationLocations/updateLocationProperty", {
          index: this.$props.number,
          property: "postalCode",
          value: value
        });
      }
    }
  }
};
</script>
