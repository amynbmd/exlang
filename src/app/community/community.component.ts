import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthenticationResponse } from '../account/_models/authentication-response';
import { Profile } from '../account/_models/profile';
import { User } from '../account/_models/user';
import { AuthenticationService } from '../account/_services/authentication/authentication.service';
import { CommunityConnectionsComponent } from '../community-connections/community-connections.component';

@Component({
  selector: 'app-community',
  templateUrl: './community.component.html',
  styleUrls: ['./community.component.css'],

  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [	
    CommonModule,
    CommunityConnectionsComponent
  ]
})
export class CommunityComponent implements OnInit {
  // users: User[] = [];
  users$: Observable<User[]>;


  constructor(private _authService:AuthenticationService) { }

  ngOnInit() {
    // this.getProfiles();

    this.users$ = this._authService.getUsersProfile(this._authService.getUserFromLocalStorage().email);
  }

  // getProfiles() {
  //   const profile1: Profile = {
  //     email: 'user1@email.com',
  //     wordofTheDay: '',
  //     isOnline: false,
  //     countryCode: 'US',
  //     picURL: './../../../assets/fake-people/person1.jpg',
  //     bio: '',
  //     nativeLang: 'en',
  //     learningLang: ['en'],
  //     level: '',
  //     interests: ['Cooking', 'Movie'],
  //     connected: false
  //   };

  //   const profile2: Profile = {
  //     email: 'user2@email.com',
  //     wordofTheDay: '',
  //     isOnline: false,
  //     countryCode: 'US',
  //     picURL: './../../../assets/fake-people/person2.jpg',
  //     bio: '',
  //     nativeLang: 'en',
  //     learningLang: ['en'],
  //     level: '',
  //     interests: ['Pets', 'Sports'],
  //     connected: false
  //   };

  //   const profile3: Profile = {
  //     email: 'user3@email.com',
  //     wordofTheDay: '',
  //     isOnline: false,
  //     countryCode: 'US',
  //     picURL: './../../../assets/fake-people/person3.jpg',
  //     bio: '',
  //     nativeLang: 'en',
  //     learningLang: ['en'],
  //     level: '',
  //     interests: ["Running", 'Rock climbing'],
  //     connected: false
  //   };

  //   const profile4: Profile = {
  //     email: 'user4@email.com',
  //     wordofTheDay: '',
  //     isOnline: false,
  //     countryCode: 'US',
  //     picURL: './../../../assets/fake-people/person4.jpg',
  //     bio: '',
  //     nativeLang: 'en',
  //     learningLang: ['en'],
  //     level: '',
  //     interests: ['Reading'],
  //     connected: false
  //   };

  //   const profile5: Profile = {
  //     email: 'user5@email.com',
  //     wordofTheDay: '',
  //     isOnline: false,
  //     countryCode: 'US',
  //     picURL: './../../../assets/fake-people/person5.jpg',
  //     bio: '',
  //     nativeLang: 'en',
  //     learningLang: ['en'],
  //     level: '',
  //     interests: [],
  //     connected: false
  //   };

  //   let user1: User = {
  //     name: 'Lowri',
  //     email: 'user1@email.com',
  //     password: '',
  //     profile: profile1
  //   };
  //   let user2: User = {
  //     name: 'Michelle',
  //     email: 'user2@email.com',
  //     password: '',
  //     profile: profile2
  //   };
  //   let user3: User = {
  //     name: 'Morgan',
  //     email: 'user3@email.com',
  //     password: '',
  //     profile: profile3
  //   };

  //   let user4: User = {
  //     name: 'Abraham',
  //     email: 'user4@email.com',
  //     password: '',
  //     profile: profile4
  //   };

  //   let user5: User = {
  //     name: 'Dude',
  //     email: 'user5@email.com',
  //     password: '',
  //     profile: profile5
  //   };

  //   this.users.push(user1);
  //   this.users.push(user2);
  //   this.users.push(user3);
  //   this.users.push(user4);
  //   this.users.push(user5);
  // }
}
