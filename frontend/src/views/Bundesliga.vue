<template>
  <v-container class="contenedor_bundesliga" fluid fill-height>
    <v-layout>
      <v-flex>
          <div class="msj_principal">
          <v-card class="mx-auto" color="#444644" dark max-width="525px">
            <v-card-title class="justify-center"> <span class="titulo">Elige los equipos e introduce las cuotas del partido.</span></v-card-title>
          </v-card>
          </div>
          <v-card class="mx-auto" color="#444644" min-width=100% dark>
          <div class="eleccion">
              <v-row align="center">
                  <v-col class="d-flex" cols="12" sm="6">
                    <v-select color="black" v-model="equipo_local" :items="items" label="Equipo Local" outlined></v-select>
                  </v-col>
                  <v-col class="d-flex" cols="12" sm="6">
                    <v-select color="black" v-model="equipo_visitante" :items="items" label="Equipo Visitante" outlined></v-select>
                  </v-col>
                </v-row>
            </div>
          </v-card>
          <v-card class="mx-auto" color="#444644" min-width=100% dark>
            <div class="cuotas">
              <v-container>
                <v-row>
                  <v-text-field color="black" v-model="cuota_local" label="Cuota equipo local" outlined persistent-hint></v-text-field>
                  <v-spacer></v-spacer>
                  <v-text-field color="black" v-model="cuota_empate" label="Cuota empate" outlined persistent-hint></v-text-field>
                  <v-spacer></v-spacer>
                  <v-text-field color="black" v-model="cuota_visitante" label="Cuota equipo visitante" outlined persistent-hint></v-text-field>
                  <v-spacer></v-spacer>
                  <v-btn color="white" class="black--text" dark v-on:click=peticionPost()>Enviar</v-btn>
                </v-row>
              </v-container>
            </div>
        </v-card>

        <v-dialog v-model="dialog" width="600px">
            <v-card>
              <v-card-title>
                <span class="headline">{{ frase_final }}</span>
              </v-card-title>
              <v-card-text>Dicho resultado ha sido calculado para el partido {{ equipo_local }} vs {{ equipo_visitante }} que tenía como cuotas {{ cuota_local }} para el {{ equipo_local }}, {{ cuota_empate }} para el empate y {{ cuota_visitante }} para el {{ equipo_visitante }}.</v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="grey" text @click="dialog = false">Vale</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>

          <v-dialog v-model="dialog2" width="600px">
            <v-card>
              <v-card-title>
                <span class="headline">No se ha podido realizar la predicción</span>
              </v-card-title>
              <v-card-text>Revisa los datos que has introducido, el equipo local no puede ser el mismo que el equipo visitante.</v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="grey" text @click="dialog2 = false">Vale</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>

      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import axios from 'axios'
  export default {
    data: () => ({
      dialog: false,
      dialog2: false,
      equipo_local: "",
      equipo_visitante: "",
      cuota_local: 1.0,
      cuota_empate: 1.0,
      cuota_visitante: 1.0,
      valor_equipo_local: 0,
      valor_equipo_visitante: 0,
      resultado: 0,
      frase_final: '',
      items: ['Borussia Dortmund',
        'Bayern Munich' ,
        'Bayern Leverkusen' ,
        'Borussia Monchengladbach' ,
        'Schalke 04' ,
        'Wolfsburg' ,
        'Hoffenheim' ,
        'Hannover 96' ,
        'Werder Bremen' ,
        'Frankfurt' ,
        'Hamburg',
        'Friburg',
        'FC Koln'
      ],
  }),

  methods: {
    peticionPost() {
      if(this.equipo_local==this.equipo_visitante){
        this.dialog2 = true;
      }
      else {
        switch(this.equipo_local){
          case 'Borussia Dortmund':
          this.valor_equipo_local = 1;
          break;
          case 'Bayern Munich':
          this.valor_equipo_local = 2;
          break;
          case 'Bayern Leverkusen':
          this.valor_equipo_local = 3;
          break;
          case 'Borussia Monchengladbach':
          this.valor_equipo_local = 4;
          break;
          case 'Schalke 04':
          this.valor_equipo_local = 5;
          break;
          case 'Wolfsburg':
          this.valor_equipo_local = 6;
          break;
          case 'Hoffenheim':
          this.valor_equipo_local = 7;
          break;
          case 'Hannover 96':
          this.valor_equipo_local = 8;
          break;
          case 'Werder Bremen':
          this.valor_equipo_local = 9;
          break;
          case 'Frankfurt':
          this.valor_equipo_local = 10;
          break;
          case 'Hamburg':
          this.valor_equipo_local = 11;
          break;
          case 'Friburg':
          this.valor_equipo_local = 12;
          break;
          case 'FC Koln':
          this.valor_equipo_local = 13;
          break;
        }

        switch(this.equipo_visitante){
          case 'Borussia Dortmund':
          this.valor_equipo_visitante = 1;
          break;
          case 'Bayern Munich':
          this.valor_equipo_visitante = 2;
          break;
          case 'Bayern Leverkusen':
          this.valor_equipo_visitante = 3;
          break;
          case 'Borussia Monchengladbach':
          this.valor_equipo_visitante = 4;
          break;
          case 'Schalke 04':
          this.valor_equipo_visitante = 5;
          break;
          case 'Wolfsburg':
          this.valor_equipo_visitante = 6;
          break;
          case 'Hoffenheim':
          this.valor_equipo_visitante = 7;
          break;
          case 'Hannover 96':
          this.valor_equipo_visitante = 8;
          break;
          case 'Werder Bremen':
          this.valor_equipo_visitante = 9;
          break;
          case 'Frankfurt':
          this.valor_equipo_visitante = 10;
          break;
          case 'Hamburg':
          this.valor_equipo_visitante = 11;
          break;
          case 'Friburg':
          this.valor_equipo_visitante = 12;
          break;
          case 'FC Koln':
          this.valor_equipo_visitante = 13;
          break;
        }
        const path = 'http://localhost:5000/api/v1.0/prediccionbundesliga'
        axios.post(path, {
        equipo_local: this.valor_equipo_local,
        equipo_visitante: this.valor_equipo_visitante,
        cuota_local: this.cuota_local,
        cuota_empate: this.cuota_empate,
        cuota_visitante: this.cuota_visitante
      })
      .then(response => {
        this.resultado = response.data
        if(this.resultado == 0){
          this.frase_final = "El ganador del encuentro será el " + this.equipo_local + "."
        }
        else if(this.resultado == 1){
          this.frase_final = "El encuentro terminará en empate."
        }
        else if(this.resultado == 2){
          this.frase_final = "El ganador del encuentro será el " + this.equipo_visitante + "."
        }
        this.dialog = true
      })
      .catch(e => {
        this.errors.push(e)
      })
      }
    },
  },
  }
</script>

<style>

.contenedor_bundesliga {
  background-image: url("https://images.unsplash.com/photo-1510051640316-cee39563ddab?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80");
  background-size: cover;
}

.cuotas {
  margin-top: 5px;
  margin-bottom: 100px;
}

</style>


