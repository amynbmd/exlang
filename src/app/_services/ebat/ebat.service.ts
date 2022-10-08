import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { EagleBankArenaTicket } from 'src/app/_models/eagle-bank-arena-ticket.model';
import { ConfigService } from 'src/app/_shared/config/config.service';

@Injectable({
  providedIn: 'root',
})
export class EbatService {
  private readonly baseUrl = this._configService.config?.apiUrl + 'eagle-bank-arena-tickets/';
  private readonly httpOptions = {
    headers: new HttpHeaders({
        "Content-Type": "application/json"
    })
  };
  
  constructor(private _http: HttpClient, private _configService: ConfigService) {}

  addTicket(ticket: EagleBankArenaTicket): Observable<EagleBankArenaTicket> {
    return this._http.post<EagleBankArenaTicket>(this.baseUrl, ticket, this.httpOptions);
  }

  getTicket(id: number): Observable<EagleBankArenaTicket> {
    return this._http.get<EagleBankArenaTicket>(this.baseUrl + id.toString(), this.httpOptions);
  }

  getTickets(): Observable<EagleBankArenaTicket[]> {
    return this._http.get<EagleBankArenaTicket[]>(this.baseUrl, this.httpOptions);
  }
}
