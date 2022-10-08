import { HttpClient } from '@angular/common/http';
import { Injectable, isDevMode } from '@angular/core';
import { firstValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ConfigService {
  private configData: AppConfig;
  private readonly configPath: string = './assets/config.json';
  constructor(
    private http: HttpClient
  ) { }

  async loadConfiguration() {
    try {
      const response = <AppConfig>await firstValueFrom(this.http.get(`${this.configPath}`));
      this.configData = response;

      if (isDevMode()) {
        this.configData.apiUrl = response.devApiUrl
      }

      return this.configData;
    } catch (err) {
      return Promise.reject(err);
    }
  }

  get config(): AppConfig {
    return this.configData;
  }
}


export interface AppConfig {
  apiUrl: string;
  devApiUrl: string;
}
