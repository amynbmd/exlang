import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { Profile } from '../account/_models/profile';
import { User } from '../account/_models/user';
import { UserCardComponent } from './user-card/user-card.component';

@Component({
  selector: 'app-community',
  templateUrl: './community.component.html',
  styleUrls: ['./community.component.css'],

  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [	
    CommonModule,
    UserCardComponent
  ]
})
export class CommunityComponent implements OnInit {
  profiles: User[] = [];

  constructor() { }

  ngOnInit() {
    this.getProfiles();
  }

  getProfiles() {
    const profile1: Profile = {
      email: 'user1@email.com',
      wordofTheDay: '',
      isOnline: false,
      countryCode: 'US',
      picURL: './../../../assets/fake-people/person1.jpg',
      bio: '',
      nativeLang: '',
      learningLang: [],
      level: '',
      interests: []  
    };

    const profile2: Profile = {
      email: 'user2@email.com',
      wordofTheDay: '',
      isOnline: false,
      countryCode: 'US',
      picURL: './../../../assets/fake-people/person2.jpg',
      bio: '',
      nativeLang: '',
      learningLang: [],
      level: '',
      interests: []  
    };

    const profile3: Profile = {
      email: 'user3@email.com',
      wordofTheDay: '',
      isOnline: false,
      countryCode: 'US',
      picURL: './../../../assets/fake-people/person3.jpg',
      bio: '',
      nativeLang: '',
      learningLang: [],
      level: '',
      interests: []  
    };

    const profile4: Profile = {
      email: 'user4@email.com',
      wordofTheDay: '',
      isOnline: false,
      countryCode: 'US',
      picURL: './../../../assets/fake-people/person4.jpg',
      bio: '',
      nativeLang: '',
      learningLang: [],
      level: '',
      interests: []  
    };

    const profile5: Profile = {
      email: 'user5@email.com',
      wordofTheDay: '',
      isOnline: false,
      countryCode: 'US',
      picURL: './../../../assets/fake-people/person5.jpg',
      bio: '',
      nativeLang: '',
      learningLang: [],
      level: '',
      interests: []  
    };

    let user1: User = {
      name: 'Lowri',
      email: 'user1@email.com',
      password: '',
      profile: profile1
    };
    let user2: User = {
      name: 'Michelle',
      email: 'user2@email.com',
      password: '',
      profile: profile2
    };
    let user3: User = {
      name: 'Morgan',
      email: 'user3@email.com',
      password: '',
      profile: profile3
    };

    let user4: User = {
      name: 'Abraham',
      email: 'user4@email.com',
      password: '',
      profile: profile4
    };

    let user5: User = {
      name: 'Dude',
      email: 'user5@email.com',
      password: '',
      profile: profile5
    };

    this.profiles.push(user1);
    this.profiles.push(user2);
    this.profiles.push(user3);
    this.profiles.push(user4);
    this.profiles.push(user5);
  }
}
